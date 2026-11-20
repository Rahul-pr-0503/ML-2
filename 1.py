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