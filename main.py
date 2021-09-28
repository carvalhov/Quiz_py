from Question import Question

questions_prompts = [
 "Qual a raiz quadrada de 121?\n(a) 9\n(b) 10\n(c) 8\n(d) 11\n\n",
 "O que e Python? \n(a) Uma linguagem\n(b) Uma mala\n(c) Uma escada\n(d) Um peixe\n\n",
 "Qual a forma da funcão afim?\n(a) y = ax²b-x\n(b) y = ax + b\n(c) x^3\n(d) ax^2+bx+c\n\n",
 "Quem estabeleceu a lei da ação e reação?\n(a) Gugu\n(b) Faustao\n(c) Isaac Newton\n(d) Faraday\n\n",
 "Quem é conhecido pela singla CR7?\n(a) Cristiano Ronaldo\n(b) Neymar\n(c) Messi\n(d) Ronaldinho Gaucho\n\n"
 ]
 
questions = [
  Question(questions_prompts[0], "d"),
  Question(questions_prompts[1], "a"),
  Question(questions_prompts[2], "b"),
  Question(questions_prompts[3], "C"),
  Question(questions_prompts[4], "a"),
]

def run_test(questions):
  score = 0
  for question in questions:
      answer = input(question.prompt)
      if answer == question.answer:
        score += 1
  
  print("Você conseguiu " + str(score) + "/" + str(len(questions)) + " corretas!")

run_test(questions)
