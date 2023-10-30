import cmd
import os
import sys
import platform
import shutil

class MyShell(cmd.Cmd):
    prompt = os.getcwd()+">"
    commands={'help':"Provides help",'exit':"exits the shell",'echo':"echo <message>\nprints the message",'know':'know <command>\ngives info about the command','cd':'cd <dir>\nmove into the directory','mkdir':'mkdir <dir>\ncreate dir'}
    def do_help(self, args):
        if len(args)==0:
            terminal_size=70
            text="Available commands:"
            padding = (terminal_size - len(text)) // 2
            print(" " * padding + text)
            print("-"*terminal_size)
            print("help",'exit',"echo","know",'exit',sep=" | ",end='\n')
        else:
            for a in list(args.split(" ")):
                print(a,":")
                print(self.commands.get(a,'unkonwn command '+str(a)),end='\n\n')
        

    def do_exit(self, args):
        print("Exiting shell.")
        return True
    
    def do_know(self,args):
        print(platform.system())
        
    def do_echo(self,args):
        print(args)
       
    def do_cd(self,args):
        try:
            os.chdir(args)
            self.prompt = os.getcwd()+">"
        except Exception:
            print("error occured")
        
    def do_mkdir(self,args):
        if len(args.split(' '))==1 and self.checkDirName(args):
            os.makedirs(args)
        else:
            print("not valid input",args)
        
    def do_dir(self,args):
        for a in os.listdir():
            print(a)
            
    def do_del(self,args):
        try:
            shutil.rmtree(args)
        except OSError as e:
            print(f"Error: {e}")
     
    def checkDirName(self,value):
        if value in os.listdir():
            print(os.listdir(),value)
            return False
        for a in value:
            a=ord(a)
            if not ((a>=65 and a<=90) or (a>=97 and a<=122) or a==95):
                return False
        return True                

if __name__ == "__main__":
    shell = MyShell()
    shell.cmdloop()
