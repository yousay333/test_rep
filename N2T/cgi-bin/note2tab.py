#!/usr/bin/env python
# coding: utf-8
import cgi
form=cgi.FieldStorage()
html_body = u"""
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8"> </head>
<body>
%s
</body>
</html>"""

###################################
######		固定値定義		#######
###################################
TRUE  = 1
FALSE = 0


##################################
#####		import			######
##################################
#ログ出力関数定義
from log import *

#クラス定義
from classes import *

##################################
#####		関数定義		######
##################################
#HTML出力
def print_html(str, *param):
	str = str%param
	print(html_body % str)
	return

#TAB出力関数
def print_TAB(str_out_TAB, coordinate):	
	print_html("<br /><br />/**** Generated TABs are shown below ****/<br />")
	for string_num in range(1, 7):
		str_out_TAB[string_num] += "-" * (MEASURE - (coordinate%MEASURE)) 
		print_html("%s|<br />", str_out_TAB[string_num])
	return

#音階をフォームから取得
def get_note(name):
	note_list = form.getlist(name)
	return note_list
	
#フォームから座標を取得
def get_coordinate(name):
    coordinate = form.getvalue(name)
    return int(coordinate)

#取得した音階をそのまま出力(すべて)
def print_note_all(NoteManager):
	for cnt in range(1, NoteManager.num+1):
		print_note(NoteManager.list[cnt].coordinate, NoteManager.list[cnt].list)
	return
	
#取得した音階をそのまま出力(1音)
def print_note(coordinate, note_list):
	if(len(note_list) is 0):
		return
	
	print_html("/**** [Cooridinate:%d]Selected notes are shown below ****/<br />", coordinate)
	for cnt in range(0,len(note_list)):
		print_html("%d : %s <br />",cnt+1, note_list[cnt])
	return

#音階管理クラス->TAB管理クラス変換
def Note2TAB_conv(NoteManager):
	#TAB管理インスタンス生成
	TABManager = TABManageClass()
	for cnt in range(1, NoteManager.num+1):
		#TAB変換
		Note2TAB = Note2TABClass(NoteManager.list[cnt])
		Note2TAB.conv2TAB()

		#TAB管理インスタンスに追加
		TABManager.add(NoteManager.list[cnt].coordinate, Note2TAB.TAB_list)
	return TABManager
	
#TAB管理クラス->出力文字管理クラス
def CreateOutputTAB(TABManager):
	#出力文字管理インスタンス生成
	Output = OutputTABClass()
	for cnt in range(1, TABManager.num+1):		
		BestTAB = TABManager.list[cnt].get_bestTAB(Output.get_latest_TAB())
		Output.add_TAB(TABManager.list[cnt].coordinate, BestTAB)

	return Output

#############################
######		実処理		#####
#############################
def main():
	#音階管理インスタンスを生成
	NoteManager = NoteManageClass()
	
	#音階を取得&管理インスタンスに追加
	NoteManager.add(get_coordinate("coordinate"), get_note("note"))
		
	#音階リストを出力
	print_note_all(NoteManager)
	
	#音階リストをTABリストに変換
	TABManager = Note2TAB_conv(NoteManager)
	
	#TABリストを元に出力用文字列管理インスタンス生成
	Output = CreateOutputTAB(TABManager)
	
	#TAB出力関数
	print_TAB(Output.OutputString, NoteManager.list[NoteManager.num].coordinate)
#	print_TAB(Output.OutputString, 1)


main()