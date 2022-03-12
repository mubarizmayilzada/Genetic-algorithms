import numpy as np
import random

gen_random = []
def generate_random(number):
    population = []
    arr = np.random.randint(0, 50, number)
    k=0
    for i in arr:
        population.append('{0:08b}'.format(i))
        k+=1
    return population

def function_value():
    X = np.linspace(-5.12, 5.12, 50)
    Ze = 0
    for i in range(len(X)):
        Ze += X[i] ** 2 - 10 * np.cos(2 * np.pi * X[i]) #Rasonbrock
    return (Ze)

def fitness_value(rand_num):
    X = np.linspace(-5.12, 5.12, 50)
    Ze = 0
    num = int(rand_num, 2)
    for i in range(len(X)):
        Ze += num**2 - 10*np.cos(2*np.pi*num)
    return(Ze)

def selection():
    fitness1 = random.choice(gen_random)
    fitness2 = random.choice(gen_random)
    
    return fitness1, fitness2

def crossover(p1, p2):
    pt = random.randint(1, len(p1) - 2)
    c1 = p1[:pt] + p2[pt:]
    c2 = p2[:pt] + p1[pt:]

    return [c1, c2]

def mutation(p1, p2):
    a = random.randint(0, 7)
    b = random.randint(0, 7)
    mut1 = []
    mut2 = []
    for i in range(8):
        mut1.append(p1[i])
        mut2.append(p2[i])

    if (mut1[a] == '0'):
        mut1[a] = '1'
    else:
        mut1[a] = '0'

    if (mut2[b] == '0'):
        mut2[b] = '1'
    else:
        mut2[b] = '0'
    result1 = ''
    result2 = ''
    for i in range(8):
        result1 +=mut1[i]
        result2 +=mut2[i]

    return result1, result2

def genetic_algorithms():


    rand = generate_random(30)

    # for i in range(30):

    for i in range(30):
        l2 = []

        for i in range(30):
            l2.append(rand[i])
            gen_random.append(l2)
            l2 = []

        for j in range(30):
            temp = abs(fitness_value(gen_random[j][0]))

            gen_random[j].append(temp)


        fit1, fit2 = selection()
        new1, new2 = crossover(fit1[0], fit2[0])
        mut3, mut4 = mutation(new1, new2)

        fit1[0] = mut3
        fit1[1] = abs(fitness_value(mut3))
        fit2[0] = mut4
        fit2[1] = abs(fitness_value(mut4))

        gen_random.sort(reverse=False)

        print("Result:", gen_random[0])

genetic_algorithms()



    
    
