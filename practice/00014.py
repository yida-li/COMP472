####################################################
# 14. : Class
####################################################

def anythingIsPossible(x):
    plausible = x + ' anything '
    return plausible


def isAnythingPossible(x):
    implaussible = x + " Is "
    return implaussible


def PossibleAnythingIs(x):
    improbable = x + " possible "
    return improbable


print(
    PossibleAnythingIs(
        isAnythingPossible(
            anythingIsPossible('i think')
        )
    )
)
