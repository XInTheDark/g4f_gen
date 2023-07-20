# https://github.com/xtekky/gpt4free

import g4f
import time

DEFAULT_PROVIDER = g4f.Provider.DeepAi

def gen_single(prompt=None, model=g4f.Model.gpt_35_turbo, provider=DEFAULT_PROVIDER, print_response=True,
               ctx=None):
    STREAM = True  # dependent on provider, currently can only be manually set
    if ctx is None and prompt is None:
        return None
    
    if ctx is None:
        ctx = [{"role": "user", "content": prompt}]
    
    # streamed completion
    response = g4f.ChatCompletion.create(model=model, messages=ctx,
                                        provider=provider,
                                        stream=STREAM) # alterative model setting
    
    if not print_response:
        return
    
    r = ""

    if STREAM:
        for message in response:
            r += message
            print(message, end="", flush=True)
    else:
        r = response
        print(response)

    return r
    

def converse(sys_prompt=None):
    ctx = []
    if sys_prompt:
        ctx.append({"role": "system", "content": sys_prompt})
    
    while True:
        prompt = input("> ")
        time_ = time.time()
        ctx.append({"role": "user", "content": prompt})
        response = gen_single(ctx=ctx)
        ctx.append({"role": "assistant", "content": response})
        print(f"\nTime: {round(time.time() - time_, 2)} seconds")


if __name__ == "__main__":
    sys_prompt = input("System prompt > ")
    converse(sys_prompt=sys_prompt)
