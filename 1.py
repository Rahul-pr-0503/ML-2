def find_s_algorithm(examples, target):
    hypothesis = ["ϕ"] * len(examples[0][0])
    for attributes, label in examples:
        if label == target:
            for i in range(len(attributes)):
                if hypothesis[i] == "ϕ":
                    hypothesis[i] = attributes[i]
                elif hypothesis[i] != attributes[i]:
                    hypothesis[i] = "?"
    return hypothesis
dataset = [
    (["Sunny", "Hot", "High", "Weak"], "No"),
    (["Sunny", "Hot", "High", "Strong"], "No"),
    (["Overcast", "Hot", "High", "Weak"], "Yes"),
    (["Rainy", "Mild", "High", "Weak"], "Yes"),
    (["Rainy", "Cool", "Normal", "Weak"], "Yes"),
    (["Rainy", "Cool", "Normal", "Strong"], "No"),
]
final_hypothesis = find_s_algorithm(dataset, "Yes")
print("Final Hypothesis (Find-S):", final_hypothesis)

def more_general(h1, h2):
    more_general_parts = []
    for x, y in zip(h1, h2):
        mg = x == "?" or (x != "ϕ" and (x == y or y == "ϕ"))
        more_general_parts.append(mg)
    return all(more_general_parts)


def candidate_elimination(examples):
    n = len(examples[0][0])
    S = ["ϕ"] * n
    G = [["?"] * n]

    for attributes, label in examples:
        if label == "Yes":
            for i in range(n):
                if S[i] == "ϕ":
                    S[i] = attributes[i]
                elif S[i] != attributes[i]:
                    S[i] = "?"

            G = [g for g in G if more_general(g, S)]

        else:
            new_G = []
            for g in G:
                for i in range(n):
                    if g[i] == "?":
                        if S[i] != "?":
                            for val in ["Sunny", "Rainy", "Overcast", "Hot", "Mild", "Cool", "High", "Normal", "Weak", "Strong"]:
                                if val != attributes[i]:
                                    new_hypothesis = g.copy()
                                    new_hypothesis[i] = val
                                    if more_general(new_hypothesis, S):
                                        new_G.append(new_hypothesis)
            G = new_G

    return S, G


dataset = [
    (["Sunny", "Hot", "High", "Weak"], "No"),
    (["Sunny", "Hot", "High", "Strong"], "No"),
    (["Overcast", "Hot", "High", "Weak"], "Yes"),
    (["Rainy", "Mild", "High", "Weak"], "Yes"),
    (["Rainy", "Cool", "Normal", "Weak"], "Yes"),
    (["Rainy", "Cool", "Normal", "Strong"], "No")
]

S, G = candidate_elimination(dataset)
print("Final Specific Boundary (S):", S)
print("Final General Boundary (G):", G)
