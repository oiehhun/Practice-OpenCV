import numpy as np

def mat_access1(mat): # 원소 직접 접근 방법
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat[i, j] # 원소 접근 -mat[i][j]와 동일
            mat[i, j] = k * 2 # 원소 할당
   
# def mat_access2(mat): # item(), itemset() 함수 사용 방법
#     for i in range(mat.shape[0]):
#         for j in range(mat.shape[1]):
#             k = mat.item(i, j) # 원소 접근
#             mat.itemset((i, j), k * 2) # 원소 할당
    
mat1 = np.arange(10).reshape(2, 5) # 0~10 사이 원소 생성
mat2 = np.arange(10).reshape(2, 5)

print("원소 처리 전: \n%s\n" % mat1)
mat_access1(mat1)
print("원소 처리 후: \n%s\n" % mat1)

# print("원소 처리 전: \n%s\n" % mat2)
# mat_access2(mat2)
# print("원소 처리 후: \n%s" % mat2)