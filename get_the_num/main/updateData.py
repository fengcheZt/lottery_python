from get_the_num.main.mid_term.inserLosingLotteryData import updateLosingLottery
from get_the_num.main.long_term.insertThripleNum import updateThripleData
from get_the_num.main.long_term.inserDHRData import updateDHR
from get_the_num.main.long_term.insertPairNum import updatePairData
from get_the_num.main.insertSSQData import updateSSQData
from get_the_num.main.blue_analyze.updateBlueOccurNum import insertBlueOccurNumData
import logging
def updateData():
    # 更新最新的数据
    updateSSQData()
    # 更新遗漏表
    updateLosingLottery()
    # 更新DHR
    updateDHR()
    # 更新成对数据
    updatePairData()
    # 更新一组3号数据
    updateThripleData()
    # 更新蓝球出现次数表
    insertBlueOccurNumData()

    logging.critical("update Data done.")
if __name__ =='__main__':
    # 更新最新的数据
    updateData()