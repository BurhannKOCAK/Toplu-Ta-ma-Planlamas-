import numpy as np

# Ağırlıklar (her kriterin önem derecesi)
weights = {
    "population_density": 0.25,      
    "existing_infrastructure": 0.2,   
    "cost": 0.2,                      
    "environmental_impact": 0.15,     
    "social_benefit": 0.2            
}

# Mahalle isimleri
districts = ["İstasyon Mahallesi", "Pınar Mahallesi", "Cumhuriyet Mahallesi"]

# Değerlendirilecek kriterler
criteria = ["population_density", "existing_infrastructure", "cost", "environmental_impact", "social_benefit"]

# Her mahalle için sentetik kriter değerleri (1-10 arasında rastgele belirlenmiştir)
data = {
    "İstasyon Mahallesi": [7, 8, 6, 4, 7],
    "Pınar Mahallesi": [5, 6, 8, 6, 5],
    "Cumhuriyet Mahallesi": [8, 7, 5, 7, 6]
}

# Softmax fonksiyonu
def softmax(scores):
    exp_scores = np.exp(scores) 
    return exp_scores / np.sum(exp_scores)  

# Her mahalle için ağırlıklı skoru hesaplama
scores = {}
for district in districts:
    weighted_sum = sum(np.array(data[district]) * np.array(list(weights.values())))
    scores[district] = weighted_sum

# Softmax fonksiyonu ile normalize edilmiş skorları hesaplama
score_values = list(scores.values())
softmax_scores = softmax(score_values)

# Sonuçları ekrana yazdırma
for idx, district in enumerate(districts):
    print(f"{district} Softmax Skoru: {softmax_scores[idx]:.4f}")

# En uygun mahalleyi seçme
best_district_idx = np.argmax(softmax_scores) 
print(f"\nEn uygun mahalle: {districts[best_district_idx]}")
