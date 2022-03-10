from utils import brute_force
from generate_plaintexts import characteristic1, characteristic2, input_list, output_list
from generate_partial_key import partial_key56, k6, k6_1, freq_k6, freq_k6_1

# Apply brute-force for remaining 14 bits of 56bits of key
final_key = brute_force(partial_key56, input_list[0], output_list[0])
if final_key == False:
    print('Key not found')
else:
    print("For characteristic =", characteristic1)
    for k in k6:
        print(k, "(6-bit key) = ", k6[k], "  frequency : ", freq_k6[k])

    print("For characteristic =", characteristic2)
    for k in k6_1:
        print(k, "(6-bit key) =",k6_1[k], "  frequency : ", freq_k6_1[k])

    print("\nPartial 56-bit key : ", partial_key56)
    print("\nFinal 56-bit key : ", final_key)
