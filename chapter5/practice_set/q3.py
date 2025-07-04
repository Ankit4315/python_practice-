# 3. Can we have a set with 18 (int) and '18' (str) as a value in it? 


st = set()
num = 123456789012345678
st.add(num)
print(st)


string = "123456789012345678"
st.add(string)

print(st)

st1 = set()
st1.add(18)
st1.add("18")
print(st1)