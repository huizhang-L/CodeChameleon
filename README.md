<!-- # CodeChamaleon -->

<h1 align="center">CodeChamaleon </h1>
A novel framework for jailbreaking in LLMs based on personalized encryption and decryption. 
<br>   <br>

<div align="center">
  <img src="paper/framework.png" alt="Logo" width="500">
</div>


## 🛠️ Usage
✨An example for jailbreaking the LLms:
```
python attack.py \
    --model_path gpt-3.5-turbo-1106 \
    --problem_path data/test_problem.csv \
    --save_path jailbreak_output \
    --encrypt_rule binary_tree \
    --prompt_style  code \
    --max_new_tokens 1024 \
    --do_sample \
    --temperature 1 \
    --repetition_penalty 1.0 \
    --top_p 0.9 \
    --use_cache \
```
✨An example for evaluating the results:
```
python gpt_evaluate.py \
    --problem_path data/test_problem.csv \
    --response_path jailbreak_output/llama2/7B/code_reverse.csv \
    --max_new_tokens 1024 \
    --temperature 1 \
    --top_p 0.9 \
```
## 🔧 Argument Specification
1. `--model_path`: The name of the model to evaluate.

2. `--problem_path`: The path of malicious problems.

3. `--save_path`: Relative path to save jailbreak results.

4. `--encrypt_rule`: Select the encrypt methods.

5. `--prompt_style`: The style of instructions (code or text).

6. `--response_path`: The path to the jailbreak output that needs to be evaluated.


The remaining parameters are all relevant parameters in the model's inference stage.
