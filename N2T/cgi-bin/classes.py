##################################
#####		固定値			######
##################################
#ギターが表現できる範囲
LOWEST_NOTE  = "L1E"
HIGHEST_NOTE = "H2B"

#各開放弦の音階     ,     1  ,   2  ,	3  ,   4  ,   5	 ,	 6
str_base_tuple=("NULL", "H1E", "M1B", "M1G", "M1D", "L1A", "L1E"  )
#全音階一覧表
#				 ド		        レ			   ミ	  ファ           ソ    			ラ  		   シ
all_note_tuple=("L2C", "L2C#", "L2D", "L2D#", "L2E", "L2F", "L2F#", "L2G", "L2G#", "L2A", "L2A#", "L2B",
				"L1C", "L1C#", "L1D", "L1D#", "L1E", "L1F", "L1F#", "L1G", "L1G#", "L1A", "L1A#", "L1B",
				"M1C", "M1C#", "M1D", "M1D#", "M1E", "M1F", "M1F#", "M1G", "M1G#", "M1A", "M1A#", "M1B",
				"H1C", "H1C#", "H1D", "H1D#", "H1E", "H1F", "H1F#", "H1G", "H1G#", "H1A", "H1A#", "H1B",
				"H2C", "H2C#", "H2D", "H2D#", "H2E", "H2F", "H2F#", "H2G", "H2G#", "H2A", "H2A#", "H2B" )

#TABにおける|の間隔
MEASURE = 16

#################################
#####		クラス定義		#####
#################################

#音階クラス
class NoteClass:
	def __init__(self, coordinate, list):
		self.coordinate = coordinate
		self.list		= list
		self.num		= len(list) 
		return
	
	def del_note(self, name):
		self.note.remove(name)
		self.num -= 1
		return
		
	def note_compensate(self, name):
		self.note.remove(name)
		idx  = all_note_tuple.index(name)
		if(idx < all_note_tuple.index(LOWEST_NOTE)):
			idx += 12
		elif(idx > all_note_tuple.index(HIGHEST_NOTE)):
			idx -= 12
		self.list.append(all_note_tuple[idx])

#音階管理クラス
class NoteManageClass:
	def __init__(self):
		self.num  = 0
		self.list = ["OFFSET"]
		return
		
	def add(self, coordinate, note_list):
		self.num += 1
		self.list.append(NoteClass(coordinate, note_list))
		return

#TABクラス
class TABClass():
	def __init__(self, coordinate, TAB_patterns):
		self.coordinate   = coordinate
		self.TAB_patterns = TAB_patterns
		return

	def get_bestTAB(self, before_TAB):
		score = []
		for cnt in range(1, len(self.TAB_patterns)):
			sum = 0
			for string_num in range(1, 7):
				before  = 0 if(before_TAB[string_num] is "-") else int(before_TAB[string_num])
				pattern = 0 if(self.TAB_patterns[cnt][string_num] is "-") else int(self.TAB_patterns[cnt][string_num])
				sum    += abs(before - pattern)
			score.append(sum)
		
		idx = score.index(min(score)) +1
		return self.TAB_patterns[idx]

#TAB管理クラス
class TABManageClass():
	def __init__(self):
		self.num  = 0
		self.list = ["OFFSET"]
		return

	def add(self, coordinate, TAB_patterns):
		self.num += 1
		self.list.append(TABClass(coordinate, TAB_patterns))
		return
		

###TAB変換クラス###
#INPUT  note_class
#OUTPUT TAB
class Note2TABClass:
	def __init__(self, note):
		self.note	  = note
		self.TAB_num  = 0
		self.TAB_list = ["OFFSET"]
		self.F_failed = 0
		return

	def conv2TAB(self):
		#前回探索時の最高音押印弦 初期値セット
		before_highest_str = 0

		#TABは最大でも5パターン
		for pattern in range(0,6):
			#ローカルTAB（追加用バッファ)
			str_out_local = ["OFFSET", "-", "-", "-", "-", "-", "-"]

			#調査済み音階数を初期化
			chk_num 		= 0

			#探索開始の弦を前回の最高音弦から１本ずらす
			target_str		= before_highest_str + 1
			
			while (target_str <= 6):
				#選択された音階の数分調査が完了したかチェック
				if(chk_num >= self.note.num):
					break

				###対象の音階が範囲内か判定###
				index_target_note = all_note_tuple.index(self.note.list[chk_num])		#探索対象の音階のインデックス
				index_str_base	  = all_note_tuple.index(str_base_tuple[target_str])	#探索対象弦のベース音階のインデックス
				pos				  = index_target_note - index_str_base					#インデックス差分で押印フレットを検出

				if ((pos>=0) &(pos<=22)):
					#本パターンにおける初回到達か判定
					if(chk_num is 0):
						before_highest_str = target_str

					#出力リストを更新
					str_out_local[target_str] = str(pos)
					#調査完了数をインクリメント
					chk_num += 1

				#調査対象弦を遷移
				target_str += 1

			#探索で１音も一致しなかった場合
			if (chk_num is 0):
				break

			#選択された全音階をTAB化できた場合
			if(chk_num is self.note.num):
				self.TAB_num += 1
				self.TAB_list.append(str_out_local)
		
		if(self.TAB_num is 0):
			F_failed = 1

		return
		

###出力文字管理クラス###
class OutputTABClass:
	def __init__(self):
		self.OutputString = ["OFFSET", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]"]
		self.before_coordinate = 0
		self.latest_TAB = ["OFFSET", "-", "-", "-", "-", "-", "-"]

	def get_latest_TAB(self):
		return self.latest_TAB

	def add_TAB(self, coordinate, BestTAB): 		
		for string_num in range(1,7):
			for writing_coo in range(self.before_coordinate +1, coordinate):
				if((writing_coo % MEASURE) is 1):
					self.OutputString[string_num] += "|-"
				else:
					self.OutputString[string_num] += "-"

			if((coordinate % MEASURE)is 1):
				self.OutputString[string_num] += "|"
		
			#coordinateの座標にTABを追加
			self.OutputString[string_num] += BestTAB[string_num]
	
		#前回値更新
		self.before_coordinate = coordinate
		self.latest_TAB = BestTAB
