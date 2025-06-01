from web3 import Web3
import json

# Kết nối Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
assert w3.is_connected()

# Nhập địa chỉ hợp đồng từ bước trước
contract_address = "0x804A10cCeC4d861d9546EAE2E35eaE3FE7E7BF7e"

# Nhập ABI từ bước trước (có thể copy từ JSON hoặc lưu vào file)
contract_abi = [
    {
        "inputs": [],
        "name": "getMessage",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "string", "name": "newMessage", "type": "string"}],
        "name": "setMessage",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "message",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    }
]

# Sử dụng tài khoản đầu tiên
w3.eth.default_account = w3.eth.accounts[0]

# Kết nối hợp đồng
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Gửi thông điệp mới
tx_hash = contract.functions.setMessage("Xin chào Blockchain!").transact()
w3.eth.wait_for_transaction_receipt(tx_hash)

# Đọc lại thông điệp
message = contract.functions.getMessage().call()
print("📩 Thông điệp đã lưu trên blockchain:", message)
