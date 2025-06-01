// contract.sol
pragma solidity ^0.8.0;

contract MessageStore {
    string public message;

    function setMessage(string memory newMessage) public {
        message = newMessage;
    }

    function getMessage() public view returns (string memory) {
        return message;
    }
}
