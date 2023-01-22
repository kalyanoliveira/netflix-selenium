from interface import Netflix

n = Netflix()
n.watch("breaking bad")

# Include this to create closing behavior
end = False
while not end:
    if input("Press enter to quit") == "":
        end = True
n.quit()

raise SystemExit