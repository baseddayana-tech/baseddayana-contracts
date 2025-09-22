// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title DAYAToken
 * @dev BasedDayana ($DAYA) ERC20 Token Contract
 * @notice This is the main token contract for the BasedDayana ecosystem
 */
contract DAYAToken is ERC20, Ownable, Pausable {
    
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    
    mapping(address => bool) public minters;
    mapping(address => bool) public burners;
    
    event MinterAdded(address indexed account);
    event MinterRemoved(address indexed account);
    event BurnerAdded(address indexed account);
    event BurnerRemoved(address indexed account);
    
    modifier onlyMinter() {
        require(minters[msg.sender], "DAYAToken: caller is not a minter");
        _;
    }
    
    modifier onlyBurner() {
        require(burners[msg.sender], "DAYAToken: caller is not a burner");
        _;
    }
    
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        require(initialSupply <= MAX_SUPPLY, "DAYAToken: initial supply exceeds max supply");
        _mint(msg.sender, initialSupply);
    }
    
    /**
     * @dev Mint tokens to a specific address
     * @param to The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyMinter whenNotPaused {
        require(totalSupply() + amount <= MAX_SUPPLY, "DAYAToken: minting would exceed max supply");
        _mint(to, amount);
    }
    
    /**
     * @dev Burn tokens from a specific address
     * @param from The address to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address from, uint256 amount) external onlyBurner whenNotPaused {
        _burn(from, amount);
    }
    
    /**
     * @dev Add a minter address
     * @param account The address to add as minter
     */
    function addMinter(address account) external onlyOwner {
        minters[account] = true;
        emit MinterAdded(account);
    }
    
    /**
     * @dev Remove a minter address
     * @param account The address to remove as minter
     */
    function removeMinter(address account) external onlyOwner {
        minters[account] = false;
        emit MinterRemoved(account);
    }
    
    /**
     * @dev Add a burner address
     * @param account The address to add as burner
     */
    function addBurner(address account) external onlyOwner {
        burners[account] = true;
        emit BurnerAdded(account);
    }
    
    /**
     * @dev Remove a burner address
     * @param account The address to remove as burner
     */
    function removeBurner(address account) external onlyOwner {
        burners[account] = false;
        emit BurnerRemoved(account);
    }
    
    /**
     * @dev Pause token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    /**
     * @dev Override transfer to include pause functionality
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
