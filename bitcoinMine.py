from hashlib import sha256
max_nonce_no = 100000000000


def sha(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_num, transaction, prev_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(max_nonce_no):
        text = str(block_num) + transaction + prev_hash + str(nonce)
        new_hash = sha(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {max_nonce_no} times")


if __name__ == '__main__':
    transaction = '''
    Dhaval->Bhavin->20
    Mando->Cara->45
    '''
    difficulty = 4
    import time
    start = time.time()
    print("Start mining")
    new_hash = mine(5, transaction, '0000185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969', difficulty)
    total_time_taken = str((time.time() - start))
    print(f"Ending the mining. Mining took: {total_time_taken} seconds")
    print(new_hash)

