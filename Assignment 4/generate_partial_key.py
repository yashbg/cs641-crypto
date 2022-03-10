from utils import str_to_bin, apply_rev_final_permutation, apply_expansion, bitwise_xor, apply_inv_permutation, find_k6_of_sboxes, key_scheduling, parity_bit_drop_table
from generate_plaintexts import output_list, output_list1

binary_output_list = [str_to_bin(c) for c in output_list]
binary_output_list1 = [str_to_bin(c) for c in output_list1]

inv_fper = [apply_rev_final_permutation(x) for x in binary_output_list]
inv_fper1 = [apply_rev_final_permutation(x) for x in binary_output_list1]

expansion_output = [apply_expansion(x[0:32]) for x in inv_fper]
expansion_output1 = [apply_expansion(x[0:32]) for x in inv_fper1]

s_box_in_xor = [bitwise_xor(expansion_output[i], expansion_output[i+1], 48) for i in range(0, len(expansion_output), 2)]
s_box_in_xor1 = [bitwise_xor(expansion_output1[i], expansion_output1[i+1], 48) for i in range(0, len(expansion_output1), 2)]

in_xor = [bitwise_xor(inv_fper[i], inv_fper[i+1], 64) for i in range(0, len(inv_fper), 2)]
f_out = [x[32:]for x in in_xor[:120]]
in_xor1 = [bitwise_xor(inv_fper1[i], inv_fper1[i+1], 64) for i in range(0, len(inv_fper1), 2)]
f_out1 = [x[32:]for x in in_xor1[:120]]

inv_perm = [apply_inv_permutation(x) for x in f_out]
inv_perm1 = [apply_inv_permutation(x) for x in f_out1]


k6, freq_k6 = find_k6_of_sboxes(s_box_in_xor, inv_perm, expansion_output, sboxes=[2, 5, 6, 7, 8])
k6_1, freq_k6_1 = find_k6_of_sboxes(s_box_in_xor1, inv_perm1, expansion_output1, sboxes=[1, 2, 4, 5, 6])

if k6["Sbox-2"] != k6_1["Sbox-2"] or k6["Sbox-5"] != k6_1["Sbox-5"] or k6["Sbox-6"] != k6_1["Sbox-6"]:
    print('More pairs required. ')
else:
    partial_k6 = [k6_1["Sbox-1"], k6_1["Sbox-2"], "######", k6_1["Sbox-4"],k6_1["Sbox-5"], k6_1["Sbox-6"], k6["Sbox-7"], k6["Sbox-8"]]
    partial_k6 = "".join(partial_k6)

    partial_key56 = ["#"] * 56
    partial_key64 = ["#"] * 64
    round_keys = key_scheduling(rounds=6)
    for i, b in enumerate(round_keys[6]):
        partial_key64[b-1] = partial_k6[i]
    for i in range(56):
        partial_key56[i] = partial_key64[parity_bit_drop_table[i]-1]
