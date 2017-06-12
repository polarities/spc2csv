import hyperspy.api as hs
import csv
import numpy as np
import os


class spc2csv():
    def convert_spc2csv(spectrum):
        """
        :return: save converted csv file with same directory of original spc file.
        """
        s = hs.load(spectrum)

        total_dataPoints = s.original_metadata.spc_header.numPts
        step = s.original_metadata.spc_header.evPerChan

        iteration = np.arange(0, (total_dataPoints - 1))

        output_path = spectrum.replace('.spc', '.csv')
        with open(output_path, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(["Energy", "Intensity"])
            for i in iteration:
                data = (i * step, s.data[i])
                writer.writerow(data)


    def get_spcFile(directory):
        """
        :return: set list that contains 'name' of every .spc file in specified directory.
        """
        list = []
        for file in os.listdir(directory):
            if file.endswith(".spc"):
                list.append(os.path.join(file))
        return list

if __name__ == "__main__":
    directory = './spcfiles'
    spc_list = spc2csv.get_spcFile(directory)

    for i in spc_list:
        spc2csv.convert_spc2csv(str(directory) + '/' + str(i))
