
 try {
        if (A > 1073741823LL) {
            Server::compute(2, 1);
            throw bad_alloc();
        }
        cout << Server::compute(A, B) << '\n';
    }
    catch (bad_alloc &e) {
        cout << "Not enough memory\n";
    }
    catch (exception &e) {
        cout << "Exception: " << e.what() << '\n';
    }
    catch (...) {
        cout << "Other Exception\n";
    }
