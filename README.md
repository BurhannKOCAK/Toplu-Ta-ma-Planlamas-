# Toplu Taşıma Hattı Planlaması - Kırklareli

Bu proje, Kırklareli'nin üç mahallesi için toplu taşıma hattı tasarımını hedefler. Softmax algoritması kullanılarak, farklı kriterler doğrultusunda en uygun güzergah belirlenmiştir. Her mahalle için beş ana kriter değerlendirilmiştir: **nüfus yoğunluğu**, **mevcut ulaşım altyapısı**, **maliyet**, **çevresel etki**, ve **sosyal fayda**.

## Proje Özeti

- **Amaç:** 
  Kırklareli'nde üç farklı mahalle için en uygun toplu taşıma hattı güzergahını belirlemek.
  
- **Kullanılan Yöntem:** 
  Softmax algoritması, mahallelerin çeşitli kriterlere göre ağırlıklı puanlarını hesaplamak ve bunları normalize etmek için kullanılmıştır. 

- **Kriterler:**
  1. **Nüfus Yoğunluğu**: Mahallenin nüfus yoğunluğu, toplu taşıma talebini etkileyen önemli bir faktördür.
  2. **Mevcut Ulaşım Altyapısı**: Mevcut altyapının durumu, yeni güzergahın inşaatı için maliyetleri etkileyebilir.
  3. **Maliyet**: Yeni güzergahın oluşturulması için gereken maliyet.
  4. **Çevresel Etki**: Çevreye olan etkiler göz önünde bulundurulmuştur.
  5. **Sosyal Fayda**: Mahallelerin toplu taşıma hattından elde edeceği sosyal fayda.

- **Mahalleler:**
  - **İstasyon Mahallesi**
  - **Pınar Mahallesi**
  - **Cumhuriyet Mahallesi**

## Kullanılan Teknolojiler

- **Python**: Proje Python dilinde yazılmıştır.
- **NumPy**: Sayısal hesaplamalar ve Softmax algoritması için kullanılmıştır.
  

