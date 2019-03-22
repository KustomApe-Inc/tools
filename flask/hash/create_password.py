from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

input_pass = input(">>> ")

hash_pass = generate_password_hash(input_pass)
# hash_passをDBにインサートします。（ここでは割愛）

print("hash: ", hash_pass)

# 下記は確認用。Trueが返ると正しく一致。Falseだと違う。
# result = check_password_hash(hash_pass, input_pass)
# print(result)