import generate
import time

def speedtest_provider(provider, prompt="Hello, how are you?", e=10):
    t = 0
    err = 0
    for i in range(e):
        try:
            time_ = time.time()
            _ = generate.gen_single(prompt=prompt, provider=provider, print_response=False)
            x = time.time() - time_
        except:
            err += 1
            print(f"Error @ {i}", end=" ", flush=True)
            continue

        t += x
        print(round(x, 2), end=" ", flush=True)
    
    if err == e:
        print(f"Error on all {e} iterations")
        return
    t = round(t / (e - err), 2)

    print(f"Epochs: {e}, Average time: {t} seconds, Errors: {err}")