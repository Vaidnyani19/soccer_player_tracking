import torch
import os
import torch.nn.functional as F

# Load features
broadcast_features = torch.load("features/broadcast_features.pt")
tacticam_features = torch.load("features/tacticam_features.pt")

# Matching results
matches = {}

print(">>> Matching players...")

for b_name, b_vec in broadcast_features.items():
    best_match = None
    best_score = -1

    for t_name, t_vec in tacticam_features.items():
        # Compute cosine similarity
        score = F.cosine_similarity(b_vec, t_vec, dim=0).item()

        if score > best_score:
            best_score = score
            best_match = t_name

    matches[b_name] = {
        "match": best_match,
        "similarity": round(best_score, 4)
    }

# Save results
os.makedirs("results", exist_ok=True)
torch.save(matches, "results/reid_matches.pt")

print("✅ Matching complete!")
print("Top 5 matches:")
for k, v in list(matches.items())[:5]:
    print(f"{k} → {v['match']} (similarity: {v['similarity']})")
