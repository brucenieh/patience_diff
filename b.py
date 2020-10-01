def save_to_csv(output_file,results):
    with open(output_file,'w') as file:
        csv_file = csv.writer(file)
        for result in results:
            for match in result[1]:
                file.write(result[0] + ',')
                csv_file.writerow(match[:-1])
    """
    Save result to a csv file

    Args:
        output_file: string, output filename
        results: list, result of all the matches
    """

    

def main():
    cwd = os.getcwd() + '/'
    results = [] # stores the result of all the matches for each file

    # parsing input argument
    parser = argparse.ArgumentParser(description='Extract dates from txt files')
    parser.add_argument('-i', '--input', type=str, help='input file directory path')
    parser.add_argument('-o', '--output',type=str, default='output.csv', help='output file directory path')
    args = parser.parse_args()

    # get all filenames
    filenames = get_filenames(args.input)
    
    # save result
    output_file_path = cwd+args.output
    save_to_csv(output_file_path,results)

if __name__ == "__main__":
    main()
