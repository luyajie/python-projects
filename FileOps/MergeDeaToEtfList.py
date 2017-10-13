print ('-------------------------------------')
dea_file_path = 'E:\\writeshare\\871m\\BenC_SecMaster\\2017-10-10\\dea.out'
etf_file_path = 'E:\\writeshare\\871m\\BenC_SecMaster\\2017-10-10\\1.csv'
final_file_path = 'E:\\writeshare\\871m\\BenC_SecMaster\\2017-10-10\\2.csv'

etf_dea_amt_map = {}
etf_ex_dt_map = {}

##
dea_file_reader = open(dea_file_path, 'r')
for line in dea_file_reader:
    if not line.startswith('#'):
        tokens = line.split('|')
        ticker_tokens = tokens[0].split(' ')
        ticker = "{0} {1}".format(ticker_tokens[0], ticker_tokens[1])
        etf_ex_dt_map[ticker] = tokens[7]
        etf_dea_amt_map[ticker] = tokens[9]
        #print("{0},{1},{2}".format(ticker, tokens[7], tokens[9]))


##

final_file_reader = open(final_file_path, 'w')
etf_file_reader = open(etf_file_path, 'r')
for line in etf_file_reader:
    tokens = line.split(',')
    #print(len(tokens))
    #print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(tokens[0],tokens[1],tokens[2],tokens[3],tokens[4],tokens[5],tokens[6],tokens[7],tokens[8],tokens[9],tokens[10],tokens[11]))

    if line.startswith('BBG_TICKER'):
        final_file_reader.write(
            "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(tokens[0], tokens[1], tokens[2], tokens[3],
                                                                       tokens[4], tokens[5], tokens[6], tokens[7],
                                                                       tokens[8], tokens[9], tokens[10], tokens[11]))
    else:
        if tokens[0] in etf_dea_amt_map:
            dea_amt = str(etf_dea_amt_map[tokens[0]])
            dea_ex_date = str(etf_ex_dt_map[tokens[0]])
        else:
            dea_amt = ''
            dea_ex_date = ''
        final_file_reader.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(tokens[0],tokens[1],tokens[2],tokens[3],tokens[4],tokens[5],tokens[6],tokens[7],tokens[8],dea_amt,dea_ex_date,tokens[11]))


dea_file_reader.close()
etf_file_reader .close()
final_file_reader.close()