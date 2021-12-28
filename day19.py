import re

''' MATRIX OPS '''

def determinant2x2(x):
    return x[0][0] * x[1][1] - x[0][1] * x[1][0]

def determinant3x3(x):
    a = x[0][0] * determinant2x2([[x[1][1], x[1][2]], [x[2][1], x[2][2]]])
    b = x[0][1] * determinant2x2([[x[1][0], x[1][2]], [x[2][0], x[2][2]]])
    c = x[0][2] * determinant2x2([[x[1][0], x[1][1]], [x[2][0], x[2][1]]])
    return a - b + c

def matmul3x3_3x1(a, b):
    ret = [[0], [0], [0]]
    for i in range(3):
        ret[i] = a[i][0] * b[0][0] + a[i][1] * b[1][0] + a[i][2] * b[2][0]
    return ret

def vec2mat(v):
    return [[x] for x in v]

def matmul3x3_3x1vec(a, vec):
    ret = [[0], [0], [0]]
    for i in range(3):
        ret[i] = a[i][0] * vec[0] + a[i][1] * vec[1] + a[i][2] * vec[2]
    return ret

rotation_matrices = []
def generate_matrices():
    cols = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    for i in range(6):
        for j in range(6):
            for k in range(6):
                mat = (
                 (cols[i][0], cols[j][0], cols[k][0]),
                 (cols[i][1], cols[j][1], cols[k][1]),
                 (cols[i][2], cols[j][2], cols[k][2]),
                )
                if determinant3x3(mat) == 1:
                    rotation_matrices.append(mat)

def get_dists(reference, target):
    for rotation_matrix in rotation_matrices:
        converted_coords = []
        for coord in target:
            converted = matmul3x3_3x1vec(rotation_matrix, coord)
            converted_coords.append(converted)

        # disabled because duplicate checking gives worse performance
        #tested = set()
        for ref_coord in reference:
            for test_coord in converted_coords:
                x = test_coord[0] - ref_coord[0]
                y = test_coord[1] - ref_coord[1]
                z = test_coord[2] - ref_coord[2]

                #hash = x * 10**8 + y * 10**4 + z
                #if hash in tested:
                #    continue
                #tested.add(hash)

                matches = 0
                for coord in converted_coords:
                    # coord at the perspective of reference coord
                    coord2 = (coord[0] - x, coord[1] - y, coord[2] - z)
                    matches += (coord2 in reference)

                if matches >= 12:
                    return rotation_matrix, x, y, z

def to0(offsets, coords, ext=(0, 0, 0)):
    parent, rotation_matrix, dx, dy, dz = offsets
    if parent == -1:
        return ext

    for i in range(len(coords)):
        coords[i] = matmul3x3_3x1vec(rotation_matrix, coords[i])
        coords[i] = (coords[i][0] - dx, coords[i][1] - dy, coords[i][2] - dz)

    ext = matmul3x3_3x1vec(rotation_matrix, ext)
    ext = (ext[0] - dx, ext[1] - dy, ext[2] - dz)

    return to0(alignment[parent], coords, ext)


with open('day19.txt', 'r') as inp:
    probes_raw = re.findall(r'--- scanner \d+ ---\n((?:[^\n]+\n)+)', inp.read())
    probes = []
    probes_final = []
    for p in probes_raw:
        probes.append(set())
        probes_final.append([])
        for q in re.findall(r'[-,\d]+', p):
            probes[-1].add(eval('(' + q + ')'))
            probes_final[-1].append(eval('(' + q + ')'))

    generate_matrices()

    alignment = {}
    alignment[0] = (-1, 0, 0, 0, 0)

    scanner_position = {}
    scanner_position[0] = (0, 0, 0)

    cache = {}
    num_of_probes = len(probes_raw)
    while len(alignment) < num_of_probes:
        for i in range(0, num_of_probes):
            for j in range(0, num_of_probes):
                #print(i, j)
                if i in alignment and j not in alignment:
                    if (i, j) not in cache:
                        cache[(i, j)] = get_dists(probes[i], probes[j])
                    if cache[(i, j)] is not None:
                        alignment[j] = (i,) + cache[(i, j)]
                        scanner_position[j] = to0(alignment[j], probes_final[j])

    # part 1
    plswork = set()
    for probe in probes_final:
        for coord in probe:
            plswork.add(coord)
    print(len(plswork))

    # part 2
    largest = 0
    for i in range(0, num_of_probes):
        for j in range(i+1, num_of_probes):
            x = abs(scanner_position[i][0] - scanner_position[j][0])
            y = abs(scanner_position[i][1] - scanner_position[j][1])
            z = abs(scanner_position[i][2] - scanner_position[j][2])
            largest = max(largest, x + y + z)
    print(largest)
