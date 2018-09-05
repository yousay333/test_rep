###################################
######		固定値定義		#######
###################################
#ログ有効/無効
LOG_ENABLE = 1
if(LOG_ENABLE):
	LVL_DEBUG = 100 
else:
	LVL_DEBUG = 0
	
LVL_WARN  = 30
LVL_ERROR = 40


##################################
#####		関数定義		######
##################################
#デバッグログ出力
import logging
def DLOG(str, *param):
	if(LOG_ENABLE):
		str  = '[D]' + str
		str  = str%param
		logging.log(LVL_DEBUG, str)
	return

#警告ログ出力
import logging
def WLOG(str, *param):
	if(LOG_ENABLE):
		str  = '[W]' + str
		str  = str%param
		logging.log(LVL_WARN, str)
	return

#エラーログ出力
import logging
def ELOG(str, *param):
	if(LOG_ENABLE):
		str  = '[E]' + str
		str  = str%param
		logging.log(LVL_ERROR, str)
	return

