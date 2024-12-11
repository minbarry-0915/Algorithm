import sys
sys.stdin = open('input.txt', 'r')

base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base64_map = {char: idx for idx, char in enumerate(base64_table)}

T = int(input())

def base64_decode(encoded_str):
    bit_buffer = 0
    bit_count = 0 
    decoded_bytes = bytearray()
    
    for char in encoded_str:
        # = 은 무시 
        if char == "=":
            continue
        
        # 6비트씩 삽입 해야되니까 기존 비트 6비트 왼쪽 시프트하고 or연산을 통해서 추가 
        bit_buffer = (bit_buffer << 6) | base64_map[char]
        bit_count += 6
        
        while bit_count >= 8:
            #가장 왼쪽에 있는 8비트만 남기기 위해서 나머지 비트만큼 오른쪽 시프트
            #마스킹으로 0으로 되어있는 왼쪽 버퍼들을 and 연산으로 삭제
            decoded_bytes.append((bit_buffer >> (bit_count - 8)) & 0xFF)
            bit_count -= 8 
    return decoded_bytes

for test_case in range(1, T+1):
    encoded_string = str(input())
    decoded_bytes = base64_decode(encoded_string)
    decoded_string = decoded_bytes.decode("utf-8")
    
    
    print(f"#{test_case} {decoded_string}")