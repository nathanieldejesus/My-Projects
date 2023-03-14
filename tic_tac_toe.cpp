#include<bits/stdc++.h>
#include <iostream>
#include <stdio.h>
using namespace std;

void add(char board[3][3],char inp,char ch)
{
	int num=inp-49,row,col;
	row=num/3,col=num%3;
	board[row][col]=ch;
}

void disp(char board[3][3])
{
	cout<<"\n\t\tPress Esc anytime to quit the game\n\n\n\n";
	int i,j;
	for(i=0;i<3;i++)
	{
		cout<<"\t\t\t\t-------------\n\t\t\t\t";
		for(j=0;j<3;j++)
		{
			if(board[i][j]=='a') cout<<"|   ";
			else
				cout<<"| "<<board[i][j]<<" ";
		}
		cout<<"|"<<endl;
	}
	cout<<"\t\t\t\t-------------\n";
}

int check(char board[3][3],char inp)
{
	int num=inp-48,row,col;
	if(num<=0 || num>=10) return 0;
	num--;
	row=num/3;
	col=num%3;
	if(board[row][col]=='a') return 1;
	else return 0;
}

char gameover(char board[3][3])
{
	char winner='a';
	if(board[0][0]==board[0][1] && board[0][0]==board[0][2] && board[0][0]!='a') winner=board[0][0];
	if(board[1][0]==board[1][1] && board[1][0]==board[1][2] && board[1][0]!='a') winner=board[1][0];
	if(board[2][0]==board[2][1] && board[2][0]==board[2][2] && board[2][0]!='a') winner=board[2][0];
	if(board[0][0]==board[1][0] && board[0][0]==board[2][0] && board[0][0]!='a') winner=board[0][0];
	if(board[0][1]==board[1][1] && board[0][1]==board[2][1] && board[0][1]!='a') winner=board[0][1];
	if(board[0][2]==board[1][2] && board[0][2]==board[2][2] && board[0][2]!='a') winner=board[0][2];
	if(board[0][0]==board[1][1] && board[0][0]==board[2][2] && board[0][0]!='a') winner=board[0][0];
	if(board[0][2]==board[1][1] && board[0][2]==board[2][0] && board[0][2]!='a') winner=board[0][2];
	return winner;
}

int draw(char board[3][3])
{
	for(int i=0;i<3;i++)
		for(int j=0;j<3;j++)
			if(board[i][j]=='a')
				return 0;
	return 1;
}

int main()
{
	cout<<"\n\n\n\n\t\t\tTic Tac Toe\n\n\n\t\tPress any key to continue";
	cin.get();
	char board[3][3],turn[2]={'X','O'},ch='X',input,winner,restart;
	do
	{
		board[0][0]=board[0][1]=board[0][2]=board[1][0]=board[1][1]=board[1][2]=board[2][0]=board[2][1]=board[2][2]='a';
		system("clear");
		disp(board);
		cout<<"\n\n\t\t\t"<<ch<<"'s Turn\n\n";
		int count=0;
		while(1)
		{
			input=cin.get();
			system("clear");
			if(input<=48 || input>=58 || !check(board,input))
			{
				disp(board);
				cout<<"\n\n\t\t\t"<<ch<<"'s Turn\n\n";
				cout<<"INVALID MOVE!!\n\n";
			}
			else
			{
				add(board,input,ch);
				disp(board);
				winner=gameover(board);
				if(winner=='a')
				{
					if(draw(board))
					{
						cout<<"\n\n\t\t\tMatch Drawn !!\n";
						break;
					}
					ch=turn[(++count)%2];
					cout<<"\n\n\t\t\t"<<ch<<"'s Turn\n\n";
				}
				else
				{
					cout<<"\n\n\t\t\t"<<winner<<" Won !!\n";
					break;
				}
			}		
		}
		cin.get();
		cout<<"\n\n\n\n\t\t\tWant to play more ? (Y/N) : ";
		cin>>restart;
	}
    while(restart=='y' || restart=='Y');
}