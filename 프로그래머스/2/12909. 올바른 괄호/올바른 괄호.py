def solution(s):
    st=[]
    if s[0] == ')':
        return False
    
    for i in s:
        if i == '(':
            st.append(i)
        else:
            if st:
                st.pop()
            else:
                return False
    return True if not st else False