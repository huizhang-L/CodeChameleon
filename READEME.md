<!-- # CodeChamaleon -->

<h1 align="center">CodeChamaleon </h1>
A novel framework for jailbreaking in LLMs based on personalized encryption and decryption. 
<br>   <br>

<div align="center">
  <img src="paper/framework.png" alt="Logo" width="500">
</div>

<!-- <h3 align="center">LOVE💗 and Peace🌊</h3>
<h3 align="center">RESEARCH USE ONLY✅ NO MISUSE❌</h3> -->


## 🛠️ Usage
✨An example run:
```
python3 main.py \
 --model_name gpt-4-0613 \
--data_path data/data_en_zh.dict \
--encode_method caesar \
--instruction_type Crimes_And_Illegal_Activities \
--demonstration_toxicity toxic \
--language en
```
## 🔧 Argument Specification
1. `--model_name`: The name of the model to evaluate.

2. `--data_path`: Select the data to run. 

3. `--encode_method`: Select the cipher to use.

4. `--instruction_type`: Select the domain of data.

5. `--demonstration_toxicity`: Select the toxic or safe demonstrations.

6. `--language`: Select the language of the data.


<!-- ## 💡Framework
<div align="center">
  <img src="paper/Overview.png" alt="Logo" width="500">
</div>



## 📃Results
The query-responses pairs in our experiments are all stored in the form of a list in the "experimental_results" folder, and torch.load() can be used to load data.
<div align="center">
  <img src="paper/main_result_demo.jpg" alt="Logo" width="500">
</div>

### 🌰Case Study
<div align="center">
  <img src="paper/case.png" alt="Logo" width="500">
</div>

### 🫠Ablation Study
<div align="center">
  <img src="paper/ablation.png" alt="Logo" width="500">
</div>

### 🦙Other Models
<div align="center">
  <img src="paper/other_models.png" alt="Logo" width="500">
</div> -->


<!-- ## 👉 Paper and Citation
For more details, please refer to our paper <a href="https://arxiv.org/abs/2308.06463">here</a>.

[![Star History Chart](https://api.star-history.com/svg?repos=RobustNLP/CipherChat&type=Date)](https://star-history.com/#RobustNLP/CipherChat&Date)

Community Discussion:
- Twitter: [AIDB](https://twitter.com/ai_database/status/1691655307892830417), [Jiao Wenxiang](https://twitter.com/WenxiangJiao/status/1691363450604457984) -->

## Citation

If you find our paper&tool interesting and useful, please feel free to give us a star and cite us through:
```bibtex

```