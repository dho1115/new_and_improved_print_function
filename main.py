from sys import stdout
from colorama import init;
from termcolor import colored;

init();
def border(borderType="*", text='INSERT TXT HERE'):
   TopAndBottomborder=borderType*len(text) + (borderType*5)
   borderedText = f"\n\n\n{TopAndBottomborder}\n{borderType} {text}  {borderType}\n{TopAndBottomborder}\n\n\n";
   return borderedText;

def print(*objects, end='\n', sep=' ', color=False, borderType=None):
   string= border(borderType=borderType, text=f'THE OUTPUT IS: {sep.join(objects[0].split())}') if borderType else f'Output from the NEW & IMPROVED Print => {sep.join(objects[0].split())}';

   if not color:
      stdout.write(string + end);
   else:
      stdout.write(colored(string, color=color, attrs=["bold", "blink"]) + end);

print("THIS SHOULD BE RED...", sep=' - ', end='\n\t===== NEW LINE HERE. =====\n', color='red');
print("This should be GREEN and have a border of 0", borderType="0", sep="/", color='green');
print("Boring old print.")





