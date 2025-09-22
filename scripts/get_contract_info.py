#!/usr/bin/env python3
"""
Script to gather detailed information about BasedDayana smart contracts
from BaseScan explorer
"""

import requests
import json
import time
from datetime import datetime

def get_contract_info(contract_address):
    """Get contract information from BaseScan"""
    try:
        # BaseScan API endpoint
        url = f"https://api.basescan.org/api?module=contract&action=getsourcecode&address={contract_address}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        if data.get('status') == '1' and data.get('result'):
            result = data['result'][0]
            return {
                "address": contract_address,
                "contract_name": result.get('ContractName', 'Unknown'),
                "compiler_version": result.get('CompilerVersion', 'Unknown'),
                "optimization_used": result.get('OptimizationUsed', 'Unknown'),
                "runs": result.get('Runs', 'Unknown'),
                "constructor_arguments": result.get('ConstructorArguments', ''),
                "evm_version": result.get('EVMVersion', 'Unknown'),
                "library": result.get('Library', ''),
                "license_type": result.get('LicenseType', 'Unknown'),
                "proxy": result.get('Proxy', '0'),
                "implementation": result.get('Implementation', ''),
                "swarm_source": result.get('SwarmSource', ''),
                "source_code": result.get('SourceCode', ''),
                "abi": result.get('ABI', ''),
                "verified": result.get('SourceCode', '') != '',
                "timestamp": datetime.now().isoformat()
            }
    except Exception as e:
        print(f"Error getting info for {contract_address}: {e}")
        return None

def get_token_info(contract_address):
    """Get token-specific information"""
    try:
        # Try to get token info
        url = f"https://api.basescan.org/api?module=token&action=tokeninfo&contractaddress={contract_address}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        if data.get('status') == '1' and data.get('result'):
            result = data['result'][0] if isinstance(data['result'], list) else data['result']
            return {
                "token_name": result.get('name', ''),
                "token_symbol": result.get('symbol', ''),
                "token_decimals": result.get('decimals', ''),
                "total_supply": result.get('totalSupply', ''),
                "token_type": "ERC20" if result.get('name') else "Unknown"
            }
    except Exception as e:
        print(f"Error getting token info for {contract_address}: {e}")
        return None

def main():
    """Main function to gather all contract information"""
    contracts = [
        "0xCF103155Ebe5358380BD946b12C8b7137ae3E2D2",  # Main token
        "0x4bbb926AA09e15E2b38d81E0d16ae09a61c0402a",
        "0x88d76b5D04eDb69bfF31a0f6Fc1D51a23BD58720",
        "0x763742DB404a5779a07dD84a9cF7Fd139ea01dba",
        "0x11e21976c28748B32dd414cf172868D19AA2bed3"
    ]
    
    all_contracts_info = {}
    
    print("🔍 Gathering contract information from BaseScan...")
    
    for i, contract in enumerate(contracts, 1):
        print(f"\n📋 Processing contract {i}/{len(contracts)}: {contract}")
        
        # Get contract info
        contract_info = get_contract_info(contract)
        if contract_info:
            all_contracts_info[contract] = contract_info
            print(f"✅ Contract info retrieved")
            
            # Try to get token-specific info
            token_info = get_token_info(contract)
            if token_info:
                all_contracts_info[contract].update(token_info)
                print(f"✅ Token info retrieved: {token_info.get('token_name', 'N/A')} ({token_info.get('token_symbol', 'N/A')})")
        else:
            print(f"❌ Failed to get contract info")
        
        # Rate limiting
        time.sleep(2)
    
    # Save to file
    output_file = "../contracts_info.json"
    with open(output_file, 'w') as f:
        json.dump(all_contracts_info, f, indent=2)
    
    print(f"\n💾 Contract information saved to {output_file}")
    
    # Print summary
    print(f"\n📊 Summary:")
    print(f"   Total contracts processed: {len(contracts)}")
    print(f"   Successful retrievals: {len(all_contracts_info)}")
    
    for contract, info in all_contracts_info.items():
        print(f"   - {contract}: {info.get('contract_name', 'Unknown')} ({info.get('token_symbol', 'N/A')})")

if __name__ == "__main__":
    main()
