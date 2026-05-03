# | ITRITR/VALOR:                                                                                     | CUENTA -> 1:      | PASOS        

# ----------------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>> ITRTR... LIST:[{'k0': [1, 2, 3]}, {'k1': [4, 5, 6]}, {'k2': [7, 8, 9]}]                         1                   1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>> ITRTR... DICT:{'k0': [1, 2, 3]}                                                                 2                   2
Value:[1, 2, 3]                                                                                     Key:k0              2
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>> ITRTR... LIST:[1, 2, 3]                                                                         3                   3
<< 1 >>                                                                                             4                   4
(==)(==)(==)(==) RETORNO(Itrtpr/Val)1                                                               4                   4
<< 2 >>                                                                                             4                   5
(==)(==)(==)(==) RETORNO(Itrtpr/Val)2                                                               4                   5
<< 3 >>                                                                                             4                   6
(==)(==)(==)(==) RETORNO(Itrtpr/Val)3                                                               4                   6
(==)(==)(==) RETORNO(Itrtpr/Val)[1, 2, 3]                                                           3                   6
<< k0 >>                                                                                            3                   7
(==)(==)(==) RETORNO(Itrtpr/Val)k0                                                                  3                   7
(==)(==) RETORNO(Itrtpr/Val){'k0': [1, 2, 3]}                                                       2                   7
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>> ITRTR... DICT:{'k1': [4, 5, 6]}                                                                 2                   8
Value:[4, 5, 6]                                                                                     Key:k1              8
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>> ITRTR... LIST:[4, 5, 6]                                                                         3                   9
<< 4 >>                                                                                             4                   10
(==)(==)(==)(==) RETORNO(Itrtpr/Val)4                                                               4                   10
<< 5 >>                                                                                             4                   11
(==)(==)(==)(==) RETORNO(Itrtpr/Val)5                                                               4                   11
<< 6 >>                                                                                             4                   12
(==)(==)(==)(==) RETORNO(Itrtpr/Val)6                                                               4                   12
(==)(==)(==) RETORNO(Itrtpr/Val)[4, 5, 6]                                                           3                   12
<< k1 >>                                                                                            3                   13
(==)(==)(==) RETORNO(Itrtpr/Val)k1                                                                  3                   13
(==)(==) RETORNO(Itrtpr/Val){'k1': [4, 5, 6]}                                                       2                   13
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>> ITRTR... DICT:{'k2': [7, 8, 9]}                                                                 2                   14
Value:[7, 8, 9]                                                                                     Key:k2              14
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>> ITRTR... LIST:[7, 8, 9]                                                                         3                   15
<< 7 >>                                                                                             4                   16
(==)(==)(==)(==) RETORNO(Itrtpr/Val)7                                                               4                   16
<< 8 >>                                                                                             4                   17
(==)(==)(==)(==) RETORNO(Itrtpr/Val)8                                                               4                   17
<< 9 >>                                                                                             4                   18
(==)(==)(==)(==) RETORNO(Itrtpr/Val)9                                                               4                   18
(==)(==)(==) RETORNO(Itrtpr/Val)[7, 8, 9]                                                           3                   18
<< k2 >>                                                                                            3                   19
(==)(==)(==) RETORNO(Itrtpr/Val)k2                                                                  3                   19
(==)(==) RETORNO(Itrtpr/Val){'k2': [7, 8, 9]}                                                       2                   19

.............. ULTIMA VUELTA....[codigo aqui antes de retornar a level()]
(==) RETORNO(Itrtpr/Val)[{'k0': [1, 2, 3]}, {'k1': [4, 5, 6]}, {'k2': [7, 8, 9]}]                   1                   19

""" --------------- FIN  Proceso R C R S V .... iterador list ... L E V E L() """

RETORNO:::: len: 30 - vueltas: 19 - num_dicc: 3 - num_itrtr= 4

[<class 'dict'>, <class 'list'>, <class 'int'>, 1, 
<class 'int'>, 2, 
<class 'int'>, 3, 
<class 'str'>, 'k0', 
<class 'dict'>, <class 'list'>, <class 'int'>, 4, 
<class 'int'>, 5, 
<class 'int'>, 6, 
<class 'str'>, 'k1', 
<class 'dict'>, <class 'list'>, <class 'int'>, 7, 
<class 'int'>, 8, 
<class 'int'>, 9, 
<class 'str'>, 'k2']