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

from abc import ABC, abstractmethod

class FormatError(Exception):
    pass

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass
    
    @abstractmethod
    def row(self, rowdata):
        pass
    
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

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')
    
    formatter.headings(fields)
    for r in records:
        rowdata =  [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

def create_formatter(fmt, column_formats=None, upper_headers=False):
    if fmt == 'text':
        formatter_cls = TextTableFormatter
    elif fmt == 'csv':
        formatter_cls = CSVTableFormatter
    elif fmt == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise FormatError('Unknown format %s' % fmt)
    
    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats
    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass
    return formatter_cls()