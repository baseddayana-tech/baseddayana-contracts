# Deployment Guide

## Overview

This document provides information about the deployment of BasedDayana smart contracts on the Base blockchain.

## Contract Addresses

### Main Token Contract
- **Contract**: DAYAToken
- **Address**: `0xCF103155Ebe5358380BD946b12C8b7137ae3E2D2`
- **Network**: Base Mainnet (Chain ID: 8453)
- **Explorer**: https://basescan.org/token/0xCF103155Ebe5358380BD946b12C8b7137ae3E2D2

### Additional Contracts

The following contracts have been deployed as part of the BasedDayana ecosystem:

1. **Address**: `0x4bbb926AA09e15E2b38d81E0d16ae09a61c0402a`
   - **Explorer**: https://basescan.org/address/0x4bbb926AA09e15E2b38d81E0d16ae09a61c0402a

2. **Address**: `0x88d76b5D04eDb69bfF31a0f6Fc1D51a23BD58720`
   - **Explorer**: https://basescan.org/address/0x88d76b5D04eDb69bfF31a0f6Fc1D51a23BD58720

3. **Address**: `0x763742DB404a5779a07dD84a9cF7Fd139ea01dba`
   - **Explorer**: https://basescan.org/address/0x763742DB404a5779a07dD84a9cF7Fd139ea01dba

4. **Address**: `0x11e21976c28748B32dd414cf172868D19AA2bed3`
   - **Explorer**: https://basescan.org/address/0x11e21976c28748B32dd414cf172868D19AA2bed3

## Network Configuration

### Base Mainnet
- **Chain ID**: 8453
- **RPC URL**: https://mainnet.base.org
- **Block Explorer**: https://basescan.org
- **Native Token**: ETH

### Base Sepolia (Testnet)
- **Chain ID**: 84532
- **RPC URL**: https://sepolia.base.org
- **Block Explorer**: https://sepolia.basescan.org

## Verification

All contracts are verified on BaseScan and their source code is publicly available through the explorer links above.

## Security

⚠️ **Important Security Notes**:

1. Always verify contract addresses before interacting with them
2. Double-check all addresses against official sources
3. Never share private keys or seed phrases
4. Use hardware wallets for large amounts
5. Test all interactions on testnet first

## Interaction Examples

### Using ethers.js

```javascript
const { ethers } = require('ethers');

const provider = new ethers.providers.JsonRpcProvider('https://mainnet.base.org');
const tokenAddress = '0xCF103155Ebe5358380BD946b12C8b7137ae3E2D2';

// ERC20 ABI (minimal)
const tokenABI = [
  'function name() view returns (string)',
  'function symbol() view returns (string)',
  'function decimals() view returns (uint8)',
  'function totalSupply() view returns (uint256)',
  'function balanceOf(address) view returns (uint256)',
  'function transfer(address to, uint256 amount) returns (bool)',
  'function approve(address spender, uint256 amount) returns (bool)'
];

const tokenContract = new ethers.Contract(tokenAddress, tokenABI, provider);

// Get token info
const name = await tokenContract.name();
const symbol = await tokenContract.symbol();
const decimals = await tokenContract.decimals();
```

### Using web3.js

```javascript
const Web3 = require('web3');

const web3 = new Web3('https://mainnet.base.org');
const tokenAddress = '0xCF103155Ebe5358380BD946b12C8b7137ae3E2D2';

// Contract ABI (same as above)
const tokenABI = [
  // ... ABI definitions
];

const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);

// Get token info
const name = await tokenContract.methods.name().call();
const symbol = await tokenContract.methods.symbol().call();
```

## Support

For technical support or questions about contract interactions, please refer to the official documentation or contact the development team through official channels.
