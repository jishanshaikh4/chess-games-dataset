# Chess Dataset

This repo contains all the chess games played by the current Chess world champion - Magnus Carlsen at lichess.org under the usernames @drnykterstein and @drdrunkenstein.  Some of the games are pre-analyzed; data is associated correspondingly.

For the sake of more games, `output_js` directory also contains all my games played on lichess under the username @jishanshaikh4.

WARNING: `output_magnus` contains 11000+ text files each file containing the data of the game in standard PGN format. Similarly, `output_js` contains 37000+ games. Of course, `lichess_js.pgn` and `lichess_magnus.png` contains all the games also.

You are more than welcome to use the games for your analysis!

## Splitting script

```python
with open('lichessjs.pgn') as fp:
	contents = fp.read()
	count = 1
	for content in contents.split('\n\n\n'):
		file = "game{}.txt".format(count)
		count = count + 1
		with open(file, 'w+') as df:
			df.write(content)
```

## Game format 

```
[Event "Rated Bullet game"]
[Site "https://lichess.org/DWpef5hg"]
[Date "2022.05.26"]
[White "jishanshaikh4"]
[Black "salirbeber"]
[Result "1-0"]
[UTCDate "2022.05.26"]
[UTCTime "13:24:36"]
[WhiteElo "2155"]
[BlackElo "2212"]
[WhiteRatingDiff "+7"]
[BlackRatingDiff "-6"]
[Variant "Standard"]
[TimeControl "60+0"]
[ECO "A45"]
[Opening "Indian Defense: Omega Gambit"]
[Termination "Time forfeit"]

1. e4 { [%clk 0:01:00] } 1... Nf6 { [%clk 0:01:00] } 2. d4 { [%clk 0:00:59] } 2... Ng8 { [%clk 0:01:00] } 3. e5 { [%clk 0:00:59] } 3... Nc6 { [%clk 0:01:00] } 4. c4 { [%clk 0:00:58] } 4... Nb8 { [%clk 0:01:00] } 5. Nf3 { [%clk 0:00:57] } 5... Na6 { [%clk 0:01:00] } 6. Nc3 { [%clk 0:00:57] } 6... Nb8 { [%clk 0:01:00] } 7. Bd3 { [%clk 0:00:57] } 7... g6 { [%clk 0:00:59] } 8. O-O { [%clk 0:00:57] } 8... Bg7 { [%clk 0:00:59] } 9. Be3 { [%clk 0:00:57] } 9... e6 { [%clk 0:00:59] } 10. Qd2 { [%clk 0:00:57] } 10... Ne7 { [%clk 0:00:59] } 11. Bh6 { [%clk 0:00:56] } 11... Bxh6 { [%clk 0:00:57] } 12. Qxh6 { [%clk 0:00:54] } 12... Nf5 { [%clk 0:00:57] } 13. Bxf5 { [%clk 0:00:53] } 13... exf5 { [%clk 0:00:56] } 14. Rfe1 { [%clk 0:00:52] } 14... Qe7 { [%clk 0:00:55] } 15. e6 { [%clk 0:00:50] } 15... Qf8 { [%clk 0:00:54] } 16. exf7+ { [%clk 0:00:48] } 16... Kd8 { [%clk 0:00:54] } 17. Re8+ { [%clk 0:00:45] } 17... Qxe8 { [%clk 0:00:51] } 18. fxe8=Q+ { [%clk 0:00:45] } 18... Rxe8 { [%clk 0:00:51] } 19. Qg5+ { [%clk 0:00:44] } 19... Re7 { [%clk 0:00:45] } 20. Re1 { [%clk 0:00:44] } 20... Nc6 { [%clk 0:00:43] } 21. Qxe7+ { [%clk 0:00:44] } 21... Nxe7 { [%clk 0:00:42] } 22. Ne5 { [%clk 0:00:43] } 22... d6 { [%clk 0:00:40] } 23. Nf7+ { [%clk 0:00:42] } 23... Kd7 { [%clk 0:00:40] } 24. Ng5 { [%clk 0:00:41] } 24... h6 { [%clk 0:00:38] } 25. Nf3 { [%clk 0:00:39] } 25... b6 { [%clk 0:00:37] } 26. b4 { [%clk 0:00:38] } 26... Ba6 { [%clk 0:00:37] } 27. c5 { [%clk 0:00:36] } 27... bxc5 { [%clk 0:00:35] } 28. dxc5 { [%clk 0:00:36] } 28... Rb8 { [%clk 0:00:34] } 29. cxd6 { [%clk 0:00:35] } 29... cxd6 { [%clk 0:00:33] } 30. a3 { [%clk 0:00:33] } 30... Rc8 { [%clk 0:00:32] } 31. Na4 { [%clk 0:00:30] } 31... Bb5 { [%clk 0:00:29] } 32. Nb2 { [%clk 0:00:28] } 32... a6 { [%clk 0:00:28] } 33. a4 { [%clk 0:00:27] } 33... Bd3 { [%clk 0:00:25] } 34. Nxd3 { [%clk 0:00:25] } 34... Nd5 { [%clk 0:00:24] } 35. b5 { [%clk 0:00:24] } 35... axb5 { [%clk 0:00:23] } 36. axb5 { [%clk 0:00:24] } 36... Rc3 { [%clk 0:00:23] } 37. Nc1 { [%clk 0:00:20] } 37... Rb3 { [%clk 0:00:22] } 38. Nxb3 { [%clk 0:00:19] } 38... Nc3 { [%clk 0:00:21] } 39. Nbd4 { [%clk 0:00:17] } 39... Nd5 { [%clk 0:00:19] } 40. Ra1 { [%clk 0:00:16] } 40... Ke7 { [%clk 0:00:18] } 41. Ra7+ { [%clk 0:00:15] } 41... Kf6 { [%clk 0:00:17] } 42. h4 { [%clk 0:00:15] } 42... g5 { [%clk 0:00:16] } 43. hxg5+ { [%clk 0:00:14] } 43... hxg5 { [%clk 0:00:16] } 44. Rd7 { [%clk 0:00:12] } 44... g4 { [%clk 0:00:14] } 45. Rxd6+ { [%clk 0:00:12] } 45... Ke7 { [%clk 0:00:13] } 46. Re6+ { [%clk 0:00:10] } 46... Kd7 { [%clk 0:00:12] } 47. Re5 { [%clk 0:00:09] } 47... Ne7 { [%clk 0:00:10] } 48. Rxe7+ { [%clk 0:00:08] } 48... Kxe7 { [%clk 0:00:10] } 49. Nxf5+ { [%clk 0:00:07] } 49... Ke6 { [%clk 0:00:09] } 50. N5d4+ { [%clk 0:00:06] } 50... Kd5 { [%clk 0:00:08] } 51. Ng5 { [%clk 0:00:05] } 51... Kc5 { [%clk 0:00:07] } 52. g3 { [%clk 0:00:05] } 52... Kb6 { [%clk 0:00:06] } 53. Nge6 { [%clk 0:00:03] } 53... Kb7 { [%clk 0:00:06] } 54. Nf5 { [%clk 0:00:03] } 54... Kb6 { [%clk 0:00:06] } 55. Ne3 { [%clk 0:00:03] } 55... Kb7 { [%clk 0:00:05] } 56. Nxg4 { [%clk 0:00:03] } 56... Kb6 { [%clk 0:00:05] } 57. Ne3 { [%clk 0:00:03] } 57... Kxb5 { [%clk 0:00:05] } 58. f4 { [%clk 0:00:03] } 58... Kc6 { [%clk 0:00:05] } 59. f5 { [%clk 0:00:03] } 59... Kd6 { [%clk 0:00:05] } 60. g4 { [%clk 0:00:03] } 60... Ke5 { [%clk 0:00:04] } 61. Kg2 { [%clk 0:00:03] } 61... Ke4 { [%clk 0:00:03] } 62. Kg3 { [%clk 0:00:03] } 62... Kxe3 { [%clk 0:00:03] } 63. Kh4 { [%clk 0:00:03] } 63... Ke4 { [%clk 0:00:02] } 64. Kg5 { [%clk 0:00:03] } 64... Ke5 { [%clk 0:00:02] } 65. Ng7 { [%clk 0:00:02] } 65... Kd6 { [%clk 0:00:02] } 66. f6 { [%clk 0:00:02] } 66... Kd7 { [%clk 0:00:01] } 67. Kg6 { [%clk 0:00:02] } 67... Kd8 { [%clk 0:00:01] } 68. Nf5 { [%clk 0:00:02] } 68... Kd7 { [%clk 0:00:00] } 69. g5 { [%clk 0:00:02] } 69... Kc6 { [%clk 0:00:00] } 70. f7 { [%clk 0:00:02] } 70... Kd5 { [%clk 0:00:00] } 71. f8=Q { [%clk 0:00:02] } 1-0
``` 
