# フィボナッチ数を再帰的に計算する
def fibonacci(n):
    # ここにフィボナッチ数列を計算するコードを書いてください。
    # Claudeに手伝ってもらおう！
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    # 5番目のフィボナッチ数を計算して表示してみよう
result = fibonacci(5)
print(result)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(f"Is {result} prime? {is_prime(result)}")
import utils.helper
