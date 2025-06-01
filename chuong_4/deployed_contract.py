from web3 import Web3
from solcx import compile_source, install_solc

# Cài compiler Solidity 0.8.0 nếu chưa có
install_solc('0.8.0')

# Đọc source code từ file contract.sol
with open('contract.sol', 'r') as file:
    contract_source_code = file.read()

# Biên dịch hợp đồng
compiled_sol = compile_source(contract_source_code, solc_version='0.8.0')
contract_id, contract_interface = compiled_sol.popitem()

# Kết nối Ganache (mặc định chạy ở 7545)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
assert w3.is_connected(), "Không kết nối được với Ganache!"

# Sử dụng tài khoản đầu tiên trong danh sách của Ganache
w3.eth.default_account = w3.eth.accounts[0]

# Tạo và triển khai hợp đồng
Contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
tx_hash = Contract.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Lưu địa chỉ và ABI để tương tác sau
contract_address = tx_receipt.contractAddress
contract_abi = contract_interface['abi']

print("✅ Hợp đồng đã triển khai tại:", contract_address)
