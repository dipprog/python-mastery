# tableformat.py

# def print_table(sequence, headers):
#     for column in headers:
#         print('%10s ' % (column), end='')
#     print()

#     print(('-'*10 + ' ')*len(headers))

#     for item in sequence:
#         for column in headers:
#             print('%10s ' % (getattr(item, column)), end='')
#         print()


# def print_table(records, fields):
#     print(' '.join('%10s' % fieldname for fieldname in fields))
#     print(('-'*10 + ' ')*len(fields))
#     for record in records:
#         print(' '.join('%10s' % getattr(record, fieldname) for fieldname in fields))

class FormatError(Exception):
    pass

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()
    
    def row(self, rowdata):
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
    
class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join('%s' % h for h in headers))

    def row(self, rowdata):
        print(','.join('%s' % d for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end=' ')
        print(' '.join(f'<th>{h}</th>' for h in headers), end=' ')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end=' ')
        print(' '.join(f'<td>{d}</td>' for d in rowdata), end=' ')
        print('</tr>')

def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata =  [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

def create_formatter(fmt):
    formatter = {
        'text': TextTableFormatter(),
        'csv': CSVTableFormatter(),
        'html': HTMLTableFormatter()
    }
    if fmt in formatter:
        return formatter[fmt]
    else:
        raise FormatError('Invalid format')
    

