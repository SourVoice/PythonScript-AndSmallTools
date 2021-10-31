quote = "I think there is a world market for maybe five computers."

print("Original quote:")
print(quote)

# 全部大写函数==============================================
print("\nIn uppercase")
print(quote.upper())

# 全部小写函数=============================================
print("\nIn lowercase:")
print(quote.lower())

# title格式函数=============================================
print("\nAs a title:")
print(quote.title())

# 指定替换函数===============================================
print("\nWith a minor replacement:")
print(quote.replace("five", "millions of"))

print("\nOriginal quote is still:")
print(quote)


print("\n" + quote.strip())
