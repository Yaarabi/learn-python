# print("Hello, World!")

# x = 5
# y = "John"

# if 1 > 2:
#     print(type(x))
# else:
#     print(type(y))
# import torch

# print("PyTorch version:", torch.__version__)
# print("CUDA available:", torch.cuda.is_available())

# with open("text.txt", "a+") as f:
#     f.write(" My name is John Doe.")
#     f.seek(0)
#     print(f.read())
#     f.close()

with open("test.js", "x") as a:
    a.write("console.log('the file created successfully')")
    a.close()

# a = open("myfile.txt", "x")
# a.write("This is a new file created with 'x' mode.\n")
# a.close()

# with open("myfile.txt", "a") as a:
#     a.write("Appending more content to the file.")
#     a.seek(0)
#     content = a.read()
#     print(content)
#open and read the file after the appending:
# with open("text.txt") as f:
#     print(f.read())

# from transformers import DPRContextEncoderTokenizer


# context_tokenizer = DPRContextEncoderTokenizer.from_pretrained('facebook/dpr-ctx_encoder-single-nq-base')

# text = [("How are you?", "I am fine."), ("What's up?", "Not much.")]

# tokens_info=context_tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=256)

# for s in tokens_info['input_ids']:
#     print(context_tokenizer.convert_ids_to_tokens(s))

# class Person:

#     sum_users = 0
#     def __init__(self, name) :
#         print("Hello bro!")
#         self.name = name
#         Person.sum_users += 1
#     def greeting(self):
#         print(f"Hello, {self.name}!")
#     def insight(self):
#             if self.name == "Youssef":
#                 print("You will be a great developer!")
#             else: 
#                 print("You need to work harder to become a great developer!")
#     def get_users(self):
#         print(f"Total users: {Person.sum_users}")

# p1 = Person("Hamid")
# p1.greeting()
# p2 = Person("Youssef")
# Person.get_users(p2)