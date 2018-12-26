from proj06 import read_file

fp = open("C.elegans_small.gff")
student_genes_list = read_file(fp)

instructor_genes_list= [('chri', 3747, 3909), ('chri', 4221, 10148), ('chri', 11641, 16585), ('chrii', 25, 175), ('chrii', 25, 175), ('chrii', 1867, 4663), ('chriii', 1271, 2917), ('chriii', 4251, 11940), ('chriii', 12189, 14753), ('chriv', 695, 14926), ('chriv', 8765, 11070), ('chriv', 15499, 20899), ('chrv', 180, 329), ('chrv', 180, 329), ('chrv', 2851, 6511), ('chrx', 151, 263), ('chrx', 151, 263), ('chrx', 13494, 13643)]
print("Instructor data:",instructor_genes_list,"\nStudent data:",student_genes_list)
assert student_genes_list == instructor_genes_list