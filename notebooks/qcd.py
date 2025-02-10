from sage.all import *

# Define the ring Z4 (integers mod 4)
Z4 = IntegerModRing(4)

# Example: Create a random generator matrix G for a linear code of length n
def generate_random_code(n, k):
    """Generates a random linear code over Z4 with generator matrix of size k x n."""
    G = random_matrix(Z4, k, n)  # k x n generator matrix
    C = LinearCode(G)  # Define the linear code
    return C

# Define code length and dimension
n = 5  # Length of codewords
k = 3  # Number of basis vectors (rank of generator matrix)

# Generate a quaternary linear code
C = generate_random_code(n, k)

# Compute the dual code
C_dual = C.dual_code()

# Check properties
is_self_dual = C == C_dual
is_self_orthogonal = C.is_self_orthogonal()
is_lcd = C.is_linear_complementary_dual()

# Display results
print("Generator Matrix:\n", C.generator_matrix())
print("Parity Check Matrix (Dual Code):\n", C_dual.generator_matrix())
print("Self-Dual:", is_self_dual)
print("Self-Orthogonal:", is_self_orthogonal)
print("LCD:", is_lcd)
