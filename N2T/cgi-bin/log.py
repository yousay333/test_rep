###################################
######		�Œ�l��`		#######
###################################
#���O�L��/����
LOG_ENABLE = 1
if(LOG_ENABLE):
	LVL_DEBUG = 100 
else:
	LVL_DEBUG = 0
	
LVL_WARN  = 30
LVL_ERROR = 40


##################################
#####		�֐���`		######
##################################
#�f�o�b�O���O�o��
import logging
def DLOG(str, *param):
	if(LOG_ENABLE):
		str  = '[D]' + str
		str  = str%param
		logging.log(LVL_DEBUG, str)
	return

#�x�����O�o��
import logging
def WLOG(str, *param):
	if(LOG_ENABLE):
		str  = '[W]' + str
		str  = str%param
		logging.log(LVL_WARN, str)
	return

#�G���[���O�o��
import logging
def ELOG(str, *param):
	if(LOG_ENABLE):
		str  = '[E]' + str
		str  = str%param
		logging.log(LVL_ERROR, str)
	return

