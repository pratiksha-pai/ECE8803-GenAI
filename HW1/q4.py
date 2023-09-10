# Define new conditional probabilities such that a/c are the same, b/a are the same, and c/b are the same.
# This would mean P(a=0|c=0) = 1, P(a=1|c=1) = 1 and so on for other variables.

# P(b | a)
P_b_given_a_strict = {
    0: {0: 1, 1: 0},
    1: {0: 0, 1: 1}
}

# P(c | b)
P_c_given_b_strict = {
    0: {0: 1, 1: 0},
    1: {0: 0, 1: 1}
}

# P(a | c)
P_a_given_c_strict = {
    0: {0: 1, 1: 0},
    1: {0: 0, 1: 1}
}

# Initialize a dictionary to store the calculated joint probabilities for all possible configurations with the new strict conditional probabilities
joint_prob_all_paths_strict = {}

# Loop through all possible values for a, b, c (0 or 1)
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            # Initialize a dictionary for each (a, b, c) configuration
            joint_prob_all_paths_strict[(a, b, c)] = {}
            
            # Calculate the joint probability for Path 1: a->b->c->a
            joint_prob_all_paths_strict[(a, b, c)]['Path 1'] = P_a_given_c_strict[c][a] * P_b_given_a_strict[a][b] * P_c_given_b_strict[b][c]
            
            # Calculate the joint probability for Path 2: b->c->a->b
            joint_prob_all_paths_strict[(a, b, c)]['Path 2'] = P_b_given_a_strict[a][b] * P_c_given_b_strict[b][c] * P_a_given_c_strict[c][a]
            
            # Calculate the joint probability for Path 3: c->a->b->c
            joint_prob_all_paths_strict[(a, b, c)]['Path 3'] = P_c_given_b_strict[b][c] * P_a_given_c_strict[c][a] * P_b_given_a_strict[a][b]

joint_prob_all_paths_strict
