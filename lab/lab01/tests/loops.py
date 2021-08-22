test = {
  'name': 'Loops',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 0:  # If this loops forever, just type Infinite Loop
          ...     n -= 1
          ...     print(n)
          2
          1
          0
          -1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> n = 4
          >>> while n > 0:  # If this loops forever, just type Infinite Loop
          ...     n += 1
          ...     print(n)
          Infinite Loop
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def go(n):
          ...     if n % 2 != 0:
          ...         print(n / 2)
          ...         return
          ...     while n > 0:
          ...         print(n)
          ...         n = n // 2
          >>> go(4)  # If this loops forever, just type Infinite Loop
          4
          2
          1
          >>> go(5)  # If this loops forever, just type Infinite Loop
          2.5
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> zero = 2
          >>> while zero != 0: # If this loops forever, just type Infinite Loop
          ...    zero = zero // 2
          ...    print(zero)
          1
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> positive = 28
          >>> while positive: # If this loops forever, just type Infinite Loop
          ...    print("positive?")
          ...    positive -= 3
          db3915202fb52c6613af5ef28bfc5773
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> positive = -9
          >>> negative = -12
          >>> while negative: # If this loops forever, just type Infinite Loop
          ...    if positive:
          ...        print(negative)
          ...    positive += 3
          ...    negative += 3
          b3c9c48be5cbc9295c81c3e75d1538d8
          efbd765b468a29852de43786a3d7f2b9
          3c05905385c5bd4c0ab5fe2640db2eed
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
