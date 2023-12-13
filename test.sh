#!/bin/bash

declare -a questions=("What is controlled by regulatory proteins that bind to regulatory elements on dna?"
                      "Fertilization is the union of a sperm and egg, resulting in the formation of what?"
                      "Where do angiosperms produce seeds in flowers?"
                      "What is the name of the process by which plants convert light energy into chemical energy?"
                      "What is the name of the substance that gives plants their green color?"
                      "What is the name of the force that causes objects to fall to the ground?"
                      "WWhat is the name of the type of chemical bond that involves the sharing of electrons between atoms?"
                      "What is the name of the law that states that the total mass of the reactants in a chemical reaction is equal to the total mass of the products?"
                      "What is the name of the process by which a solid substance changes directly into a gas without passing through the liquid state?"
                      "What is the name of the smallest particle of an element that retains its chemical properties?")

for question in "${questions[@]}"
do
  curl --location 'localhost:5500/execution' \
       --header 'Content-Type: application/json' \
       --data '{
           "text":["'"$question"'"]
       }' &
  sleep 1
done