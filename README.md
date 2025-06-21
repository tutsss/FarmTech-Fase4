# 🌱 FarmTech Solutions – Fase 4

Projeto desenvolvido para a disciplina de Gestão do Agronegócio - FIAP  
**Objetivo:** Aplicar técnicas de data science e IoT para aprimorar um sistema inteligente de irrigação.

---

## 🔧 Melhorias da Fase 4

- 🔍 **Scikit-learn**: modelo preditivo de irrigação baseado em dados históricos de sensores.
- 📊 **Streamlit**: dashboard interativo para visualizar dados e previsão.
- 📟 **LCD I2C**: exibe informações críticas no display (umidade, nutrientes, status).
- 📈 **Serial Plotter**: monitoramento em tempo real de variáveis do sistema.
- ⚙️ **Código ESP32 otimizado**: tipos de dados ajustados para uso eficiente de memória.
- 💾 **Banco de dados**: estruturado para armazenar dados de sensores (expansível).

---

## 📌 Componentes simulados no Wokwi

- ESP32
- 2 Potenciômetros (umidade e nutrientes)
- LCD I2C 16x2
- LED com resistor de 220Ω (simulando relé)

🧪 Simulação disponível:  
🔗 [Clique para abrir no Wokwi](https://wokwi.com/projects/434250200665990145)

---

## 💡 Modelo preditivo

O modelo foi treinado usando um `DecisionTreeClassifier` da biblioteca **Scikit-learn**, com dados simulados:

| Umidade (%) | Nutrientes (%) | Irrigar |
|-------------|----------------|---------|
| 20          | 25             | Sim     |
| 45          | 60             | Não     |
| ...         | ...            | ...     |

## 🖥️ Dashboard com Streamlit

- Interface amigável para operadores agrícolas
- Insere valores de sensores manualmente
- Exibe se é necessário irrigar ou não
- Mostra gráfico de tendências

### Execução local:
```bash
pip install streamlit pandas scikit-learn joblib
streamlit run app.py
