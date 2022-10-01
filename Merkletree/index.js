const { MerkleTree } = require('merkletreejs');
const keccak256 = require('keccak256');
const whitelistJson = require('./whitelist.json');

const addresses = JSON.parse(whitelistJson["whitelist"]);
const leaves = addresses.map(addr => keccak256(addr))

const merkleTree = new MerkleTree(leaves, keccak256, { sortPairs: true })

const rootHash = merkleTree.getRoot()

console.log(merkleTree.toString())


let claimingAddress = leaves[0]
let proof = merkleTree.getHexProof(claimingAddress)
console.log(proof)

console.log(merkleTree.getHexRoot())
//console.log(proof);

console.log(merkleTree.verify(proof, claimingAddress, rootHash))

/*
0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2

0x74f4666169faccda89a45d47ab1997a62f24c3cd534a01539db8f0e40d3eb8b1
*/
